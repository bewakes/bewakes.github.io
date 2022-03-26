function load()
{
    g_searchbox.style.visibility="hidden"; 
    $("#search-result").hide();
}

// when search icon is clicked, set placeholder and focus
function searchIconClick()
{
    if (g_searchbox.style.visibility == "visible") {
        g_searchbox.style.visibility="hidden";
        $('#search-result').hide();
    }
    else {
        g_searchbox.style.visibility="visible";
        g_searchbox.focus();
    }
}

// function gets json data from server(search results) and populates'em
function populateSearchResult(jsondata)
{
    var searchlist = document.getElementById("search-result-list");
    // first clear the previous results
    var childs = searchlist.children;
    for (var i=0;i<childs.length;i++)
        searchlist.removeChild(childs[i]);

    data = jsondata.data;
    if (data.length==0) 
    {   $("#search-result").hide(); 
        return;
    }

    $("#search-result").show();

    for(var i=0;i<data.length;i++)
    {
        var li = document.createElement("li");
        li.setAttribute("class", "list-group-item");
        var a = document.createElement("a");
        a.setAttribute("href", "/blog/"+ data[i].slug);
        a.className = 'search-result-link';
        a.innerHTML = data[i].title;
        li.appendChild(a);
        searchlist.appendChild(li);
    }
}
