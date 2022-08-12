(function () {
    const slideList = document.querySelector(".slide_list"); // Slide parent dom
    const slideContents = document.querySelectorAll(".slide_content"); // each slide dom
    const slideBtnNext = document.querySelector(".fa-solid fa-circle-right icon"); // next button
    const slideBtnPrev = document.querySelector(".fa-solid fa-circle-left icon"); // prev button
    const pagination = document.querySelector(".slide_pagination");
    const slideLen = slideContents.length; // slide length
    const slideWidth = 400; // slide width
    const slideSpeed = 300; // slide speed
    const startNum = 0; // initial slide index (0 ~ 4)

    slideList.style.width = slideWidth * (slideLen + 2) + "px";

    // Copy first and last slide
    let firstChild = slideList.firstElementChild;
    let lastChild = slideList.lastElementChild;
    let clonedFirst = firstChild.cloneNode(true);
    let clonedLast = lastChild.cloneNode(true);

    // Add copied Slides
    slideList.appendChild(clonedFirst);
    slideList.insertBefore(clonedLast, slideList.firstElementChild);


    /** Next Button Event */
    slideBtnNext.addEventListener("click", function () {
        if (curIndex <= slideLen - 1) {
            slideList.style.transition = slideSpeed + "ms";
            slideList.style.transform =
                "translate3d(-" + slideWidth * (curIndex + 2) + "px, 0px, 0px)";
        }
        if (curIndex === slideLen - 1) {
            setTimeout(function () {
                slideList.style.transition = "0ms";
                slideList.style.transform =
                    "translate3d(-" + slideWidth + "px, 0px, 0px)";
            }, slideSpeed);
            curIndex = -1;
        }
        curSlide.classList.remove("slide_active");
        pageDots[curIndex === -1 ? slideLen - 1 : curIndex].classList.remove(
            "dot_active"
        );
        curSlide = slideContents[++curIndex];
        curSlide.classList.add("slide_active");
        pageDots[curIndex].classList.add("dot_active");
    });

    /** Prev Button Event */
    slideBtnPrev.addEventListener("click", function () {
        if (curIndex >= 0) {
            slideList.style.transition = slideSpeed + "ms";
            slideList.style.transform =
                "translate3d(-" + slideWidth * curIndex + "px, 0px, 0px)";
        }
        if (curIndex === 0) {
            setTimeout(function () {
                slideList.style.transition = "0ms";
                slideList.style.transform =
                    "translate3d(-" + slideWidth * slideLen + "px, 0px, 0px)";
            }, slideSpeed);
            curIndex = slideLen;
        }
        curSlide.classList.remove("slide_active");
        pageDots[curIndex === slideLen ? 0 : curIndex].classList.remove(
            "dot_active"
        );
        curSlide = slideContents[--curIndex];
        curSlide.classList.add("slide_active");
        pageDots[curIndex].classList.add("dot_active");
    });

})();
