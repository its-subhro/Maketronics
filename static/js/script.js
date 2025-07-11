function filterTools() {
    var input = document.getElementById("filterInput");
    var filter = input.value.toLowerCase();
    var ol = document.getElementById("toolList");
    var li = ol.getElementsByTagName("li");

    var toolsArray = Array.from(li);

    ol.innerHTML = "";

    toolsArray.forEach(function (item) {
        var toolName = item.textContent || item.innerText;
        if (toolName.toLowerCase().startsWith(filter)) {
            ol.appendChild(item);
        }
    });
}