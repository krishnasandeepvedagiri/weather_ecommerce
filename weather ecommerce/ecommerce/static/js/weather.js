let loc = document.getElementById("search-input");
let tempvalue = document.getElementById("temp-value");
const searchButton = document.getElementById("search-button");


const getWeather = async(city)=>{
    try{
    const proxy = "https://cors-anywhere.herokuapp.com/corsdemo"

    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=63a65210583445a0a62c9b64f74dc2f2`, {node: 'corsdemo'});

    var weatherData = await response.json();
    console.log(weatherData);
    const{name}=weatherData;
    const{feels_like}=weatherData.main;
    // const{id,main}=weatherData.weather[0];

    loc.textContent=name;
    // climate.textContent=main;
    tempvalue.textContent=Math.round(feels_like-273);



    // console.log(data)


    
// function submitTemp() {
    // let tv = document.getElementById("temp-value").value;
    let tv = Math.round(feels_like-273);
    console.log(tv)
    // alert(tv)
    // var t=0;
    // if (tempValue == null) {
    // 	t = 0.0;
    // } else if (tempValue < 10) {
    // 	t = 1.0;
    // } else if (tempValue >= 10 && tempValue < 20) {
    // 	t = 2.0;
    // } else if (tempValue >= 20 && tempValue < 30) {
    // 	t = 3.0;
    // } else if (tempValue >= 30 && tempValue < 40) {
    // 	t = 4.0;
    // } else {
    // 	t = 5.0;
    // }

    fetch('/api/mydata/')
    .then(response => response.json())
    .then(data => console.log(data));

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // handle the response from the backend
            // document.getElementsByClassName("row").innerHTML = this.responseText;
            console.log(this.responseText);
            var response = JSON.parse(this.responseText);
        
            // get the length of the products array
            var p = response.products.length;
            var productsHTML = "";
			for (var i = 0; i < p; i++) {
				var product = response.products[i];
				if (product.tag == this.t ) {
					var productHTML = `
						<div class="col-lg-4">
							<img class="thumbnail" src="${product.imageURL}">
							<div class="box-element product">
								<h6><strong>${product.name}</strong></h6>
								<hr>
								<button data-product="${product.id}" data-action="add" class="btn btn-outline-secondary add-btn update-cart">Add to Cart</button>
								<h4 style="display: inline-block; float: right"><strong>₹${product.price.toFixed(2)}</strong></h4>
							</div>
						</div>
					`;
					productsHTML += productHTML;
				}
			}
            var row = document.getElementsByClassName("row")[0];
			row.innerHTML = productsHTML;



        }
    };
    xhttp.open("POST", "/submit_output/", true);
    var csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("tv=" + tv);

    // function to get the CSRF token from the cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // check if the cookie name matches the required name
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }




    }
    catch{
        alert("City Not Found")
    }

}

// const recommend{
    
// }

searchButton.addEventListener('click',(e)=>
{
    e.preventDefault();
    getWeather(loc.value);
    // recommend(tempvalue.value);
    loc.value='';
// })

});