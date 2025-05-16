document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("finalizeModal");
    const closeBtn = document.getElementById("closeModal");
    const steps = document.querySelectorAll(".form-step");
    const form = document.getElementById("finalizeForm");

    function showStep(index) {
        steps.forEach((s, i) => {
            s.style.display = i === index - 1 ? "block" : "none";
        });
    }

    window.nextStep = showStep;

    document.querySelectorAll(".finalize-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const offerId = btn.dataset.offerId;

            // Update the form action to point to the correct URL
            form.action = `/accounts/profile/finalize_offer/${offerId}/`;

            // Show modal with flex to center content
            modal.style.display = "flex";
            showStep(1);
        });
    });

    closeBtn.onclick = () => modal.style.display = "none";

    window.onclick = (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };
});

document.getElementById('id_paymentMethod').addEventListener('change', function () {
    const method = this.value;
    document.getElementById('creditCardFields').style.display = (method === 'Credit Card') ? 'block' : 'none';
    document.getElementById('bankFields').style.display = (method === 'Bank Transfer') ? 'block' : 'none';
    document.getElementById('mortgageFields').style.display = (method === 'Mortgage') ? 'block' : 'none';
});
