// function submitTemp(){
    
//     var tempValue = document.getElementById("temp-value").value;
//     var t=0;

//     if (tempValue < 10) {
//         t = "1.0";
//     } else if (tempValue >= 10 && tempValue < 20) {
//         t = "2.0";
//     } else if (tempValue >= 20 && tempValue < 30) {
//         t = "3.0";
//     } else if (tempValue >= 30 && tempValue < 40) {
//         t = "4.0";
//     } else {
//         t = "5.0";
//     }


//     function updateOutput(value) {
//         document.getElementsByClassName("row").innerHTML = "
//         {% for product in products %}
// 		{% if {{product.tag}} == (t or 0.0) }
// 		<div class="col-lg-4">
// 			<img class="thumbnail" src="{{product.imageURL}}">
// 			<div class="box-element product">
// 				<h6><strong>{{product.name}}</strong></h6>
// 				<hr>

// 				<button data-product="{{product.id}}" data-action="add" class="btn btn-outline-secondary add-btn update-cart">Add to Cart</button>
// 				<!-- <a class="btn btn-outline-success" href="#">View</a> -->
// 				<h4 style="display: inline-block; float: right"><strong>
// 					₹{{product.price|floatformat:2}}
// 				</strong></h4>

// 			</div>
// 		</div>


// 		{% endfor %}";
//     }

//     updateOutput(t);

// }
