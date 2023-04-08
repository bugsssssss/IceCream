let menuBtn = document.querySelector(".menu-btn");
let menu = document.querySelector(".menu");

menuBtn.addEventListener("click", function () {
	menuBtn.classList.toggle("active");
	menu.classList.toggle("active");
});

var splide = new Splide(".splide", {
	type: "loop",
	perPage: 1,
	perMove: 1,
	snap: (boolean = true),
	arrows: false,
	autoplay: true,
	interval: 7000,
	speed: 5000,
	resetProgress: (boolean = false),
});
splide.mount();

let wrapperPopUp__one = document.querySelector(".wrapperPopUp__one");
let wrapperPopUp__two = document.querySelector(".wrapperPopUp__two");
let linkEnterBtn = document.querySelector(".linkEnterBtn");
let aReg = document.querySelector(".aReg");
let aEnt = document.querySelector(".aEnt");

linkEnterBtn.addEventListener("click", showPopUp__ent);
aReg.addEventListener("click", showPopUp__reg);
aEnt.addEventListener("click", showPopUp__ent);
wrapperPopUp__one.addEventListener("click", closePopUp);
wrapperPopUp__two.addEventListener("click", closePopUp);

function showPopUp__ent() {
	wrapperPopUp__two.classList.remove("active__wrapperPopUp");
	wrapperPopUp__one.classList.add("active__wrapperPopUp");
}
function showPopUp__reg() {
	wrapperPopUp__one.classList.remove("active__wrapperPopUp");
	wrapperPopUp__two.classList.add("active__wrapperPopUp");
}
function closePopUp() {
	let elem = event.target;
	if (elem == wrapperPopUp__one || elem == wrapperPopUp__two) {
		wrapperPopUp__one.classList.remove("active__wrapperPopUp");
		wrapperPopUp__two.classList.remove("active__wrapperPopUp");
	}
}
