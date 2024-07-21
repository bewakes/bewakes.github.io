--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}

import Data.Monoid ((<>))
import Hakyll
import Hakyll.Core.Identifier(Identifier)
import System.FilePath (replaceExtension, takeBaseName, takeDirectory, (</>))
import System.Process
import Text.Pandoc (ReaderOptions (readerExtensions), WriterOptions (writerExtensions))
import Text.Pandoc.Extensions (enableExtension)
import Text.Pandoc.Highlighting (Style, breezeDark, espresso, styleToCss)
import Text.Pandoc.Options
import Hakyll.Core.Logger (debug)
import Debug.Trace (trace)
import System.FilePath.Posix (takeFileName, dropExtension)

config :: Configuration
config = defaultConfiguration
  { destinationDirectory = "docs"
  }

--------------------------------------------------------------------------------
main :: IO ()
main = hakyllWith config $ do
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
      let identiconCtx = getIdenticonCtx path
      pandocCompilerWith hakyllReaderOptions hakyllWriterOptions
        >>= loadAndApplyTemplate "templates/post.html" (postCtx <> identiconCtx)
        >>= loadAndApplyTemplate "templates/default.html" postCtx

  -- Compile posts and extract tags
  tags <- buildTags "posts/*" (fromCapture "tags/*.html")

  tagsRules tags $ \tag pattern -> do
    let title = "Tagged: " ++ tag
    route cleanRoute
    compile $ do
        posts <- recentFirst =<< loadAll pattern
        let ctx = constField "title" title <>
                  listField "posts" (postCtxWithTags tags) (return posts) <>
                  defaultContext
        makeItem ""
            >>= loadAndApplyTemplate "templates/posts.html" ctx
            >>= loadAndApplyTemplate "templates/default.html" ctx

  create ["tags.html"] $ do
    route cleanRoute
    compile $ do
      let tagCtx = field "title" (return . itemBody) <> field "url" (\item -> return $ "/tags/" ++ itemBody item)
      let postsCtx =
              listField "tags" tagCtx (mapM makeItem_ $ tagsMap tags) <>
              defaultContext
      makeItem ""
          >>= loadAndApplyTemplate "templates/tags.html" postsCtx
          >>= loadAndApplyTemplate "templates/default.html" postsCtx

  create ["posts.html"] $ do
    route cleanRoute
    compile $ do
      posts <- recentFirst =<< loadAll "posts/*"
      let postsCtx =
              listField "posts" postCtx (return posts) <>
              constField "title" "All Posts" <>
              defaultContext
      makeItem ""
          >>= loadAndApplyTemplate "templates/posts.html" postsCtx
          >>= loadAndApplyTemplate "templates/default.html" postsCtx

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

  match "now.html" $ do
    route cleanRoute
    compile $ do
      getResourceBody
        >>= applyAsTemplate defaultContext
        >>= loadAndApplyTemplate "templates/default.html" defaultContext

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

getIdenticonCtx :: FilePath -> Context String
getIdenticonCtx path = constField "identicon" (transformPath path) <> defaultContext

-- Function to transform a markdown file path to an image file path
transformPath :: FilePath -> FilePath
transformPath mdPath =
  let baseName = takeBaseName mdPath
   in "images" </> (baseName ++ ".png")

postCtxWithTags :: Tags -> Context String
postCtxWithTags tags = tagsField "tags" tags <> defaultContext

-- Custom route to remove .html extension
cleanRoute :: Routes
cleanRoute = customRoute $ createIndexRoute . toFilePath
  where
    createIndexRoute p = takeDirectory p </> takeFileName (dropExtension p) </> "index.html"

makeItem_ :: (String, [Identifier]) -> Compiler (Item String)
makeItem_ (x, i:_) = return $ Item {itemIdentifier= i, itemBody=x}
