let text_submit_form = document.querySelector("#text_submit_form");

text_submit_form.addEventListener("submit", function (event) {
	event.preventDefault();
	let result_container = document.querySelector("#result_container");
	if (result_container.querySelector("#result") !== null) {
		let child_element = document.querySelector("#result");
		result_container.removeChild(child_element);
	}
	let comparator = document.querySelector("#similarity_measure");
	let text1 = document.querySelector("#input_string_1");
	let text2 = document.querySelector("#input_string_2");

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
			let result = document.createElement("p");
			result.setAttribute("id", "result");
			result.innerText = "Similarity index: " + response;
			let container = document.querySelector("#result_container");
			container.appendChild(result);
		});
});
