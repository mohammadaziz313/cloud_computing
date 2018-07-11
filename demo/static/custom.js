//Custom Javascript File

function showCat(){
    var x = document.getElementById("imageView");
    x.innerHTML='<img src="{{url_for("static", filename="assests/images/cat_image.jpg")}}" height="200px" />';
}