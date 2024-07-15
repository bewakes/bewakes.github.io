--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}

import Data.Monoid ((<>))
import Hakyll
import System.FilePath (replaceExtension, takeBaseName, takeDirectory, (</>))
import System.Process
import Text.Pandoc (ReaderOptions (readerExtensions), WriterOptions (writerExtensions))
import Text.Pandoc.Extensions (enableExtension)
import Text.Pandoc.Highlighting (Style, breezeDark, espresso, styleToCss)
import Text.Pandoc.Options

--------------------------------------------------------------------------------
main :: IO ()
main = hakyll $ do
  match "images/*" $ do
    route idRoute
    compile copyFileCompiler

  match "css/*" $ do
    route idRoute
    compile compressCssCompiler

  match "posts/*" $ do
    route $ setExtension "html"
    compile $ do
      path <- getResourceFilePath
      unsafeCompiler $ do
        generateIdenticon path
      let identiconCtx = generateIdenticonCtx path
      pandocCompilerWith hakyllReaderOptions hakyllWriterOptions
        >>= loadAndApplyTemplate "templates/post.html" (postCtx <> identiconCtx)
        >>= loadAndApplyTemplate "templates/default.html" postCtx
        >>= relativizeUrls

  create ["archive.html"] $ do
    route idRoute
    compile $ do
      posts <- recentFirst =<< loadAll "posts/*"
      let archiveCtx =
            listField "posts" postCtx (return posts)
              <> constField "title" "Archives"
              <> defaultContext

      makeItem ""
        >>= loadAndApplyTemplate "templates/archive.html" archiveCtx
        >>= loadAndApplyTemplate "templates/default.html" archiveCtx
        >>= relativizeUrls

    create ["css/syntax.css"] $ do
        route idRoute
        compile $ do
            makeItem $ styleToCss pandocCodeStyle

  match "index.html" $ do
    route idRoute
    compile $ do
      posts <- recentFirst =<< loadAll "posts/*"
      let indexCtx =
            listField "posts" postCtx (return posts)
              <> defaultContext

      getResourceBody
        >>= applyAsTemplate indexCtx
        >>= loadAndApplyTemplate "templates/default.html" indexCtx
        >>= relativizeUrls

  match "now.html" $ do
    route idRoute
    compile $ do
      getResourceBody
        >>= applyAsTemplate defaultContext
        >>= loadAndApplyTemplate "templates/default.html" defaultContext
        >>= relativizeUrls

  match "templates/*" $ compile templateBodyCompiler

hakyllReaderOptions :: ReaderOptions
hakyllReaderOptions =
  defaultHakyllReaderOptions
    { readerExtensions =
        enableExtension Ext_tex_math_dollars
          . enableExtension Ext_latex_macros
          . enableExtension Ext_tex_math_double_backslash
          . enableExtension Ext_tex_math_single_backslash
          $ readerExtensions defaultHakyllReaderOptions
    }

hakyllWriterOptions :: WriterOptions
hakyllWriterOptions =
  defaultHakyllWriterOptions
    { writerExtensions =
        enableExtension Ext_tex_math_dollars
          . enableExtension Ext_latex_macros
          . enableExtension Ext_tex_math_double_backslash
          . enableExtension Ext_tex_math_single_backslash
          $ writerExtensions defaultHakyllWriterOptions,
      writerHighlightStyle = Just pandocCodeStyle
    }

pandocCodeStyle :: Style
pandocCodeStyle = espresso

--------------------------------------------------------------------------------
postCtx :: Context String
postCtx =
  dateField "date" "%B %e, %Y"
    <> defaultContext

generateIdenticon :: FilePath -> IO ()
generateIdenticon route = do
  callCommand $ "python3 scripts/identicon.py " ++ route

generateIdenticonCtx :: FilePath -> Context String
generateIdenticonCtx path = constField "identicon" (transformPath path) <> defaultContext

-- Function to transform a markdown file path to an image file path
transformPath :: FilePath -> FilePath
transformPath mdPath =
  let baseName = takeBaseName mdPath
   in "/images" </> (baseName ++ ".png")
