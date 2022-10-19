let text_submit_form = document.querySelector("#text_submit_form");

text_submit_form.addEventListener("submit", function (event) {
	event.preventDefault();
	let comparator = document.querySelector("#similarity_measure");
	let text1 = document.querySelector("#input_string_1");
	let text2 = document.querySelector("#input_string_2");
	// console.log(text1.value);

	fetch(
		"/input?comparator=" +
			comparator.value +
			"&text1=" +
			text1.value +
			"&text2=" +
			text2.value
	)
		.then((response) => response.json())
		.then((response) => {
			console.log(response);
			// let result_container

			let result = document.createElement("p");
			result.innerText = "Similarity index: " + response;
			console.log(result);

			let container = document.querySelector("#result_container");
			container.appendChild(result);
		});

	// let user = document.querySelector("#user_name");
	// get_user(user.value);
	// lookup_form.reset();
});
