document.addEventListener("DOMContentLoaded", function () {
    const openBtn = document.getElementById("openOfferModal");
    const closeBtn = document.getElementById("closeModal");
    const modal = document.getElementById("offerModal");

    if (openBtn && closeBtn && modal) {
        openBtn.onclick = () => {
            modal.style.display = "block";
        };

        closeBtn.onclick = () => {
            modal.style.display = "none";
        };

        window.onclick = (event) => {
            if (event.target === modal) {
                modal.style.display = "none";
            }
        };
    }
});
