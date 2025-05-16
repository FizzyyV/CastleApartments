document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("finalizeModal");
    const closeBtn = document.getElementById("closeModal");
    const steps = document.querySelectorAll(".form-step");
    const form = document.getElementById("finalizeForm");

    function showStep(index) {
        steps.forEach((s, i) => {
            s.style.display = i === index - 1 ? "block" : "none";
        });

        // Show review content when on step 4
        if (index === 4) {
            const review = document.getElementById('reviewContent');
            review.innerHTML = `
                <h3>Contact Info</h3>
                <p><strong>National ID:</strong> ${document.getElementById('id_nationalId').value}</p>
                <p><strong>Phone Number:</strong> ${document.getElementById('id_phoneNumber').value}</p>

                <h3>Address</h3>
                <p><strong>Street Name:</strong> ${document.querySelector('input[name="street_name"]').value}</p>
                <p><strong>City:</strong> ${document.querySelector('input[name="city"]').value}</p>
                <p><strong>Postal Code:</strong> ${document.querySelector('input[name="postal_code"]').value}</p>
                <p><strong>Country:</strong> ${document.getElementById('country').value}</p>

                <h3>Payment</h3>
                <p><strong>Method:</strong> ${document.getElementById('id_paymentMethod').value}</p>
                ${getPaymentDetailsHTML()}
            `;
        }
    }

    function getPaymentDetailsHTML() {
        const method = document.getElementById('id_paymentMethod').value;
        let html = '';
        if (method === 'Credit Card') {
            html = `
                <p><strong>Cardholder:</strong> ${document.querySelector('input[name="cardholder"]').value}</p>
                <p><strong>Card Number:</strong> ${document.querySelector('input[name="card_number"]').value}</p>
                <p><strong>Expiry Date:</strong> ${document.querySelector('input[name="card_expiry"]').value}</p>
                <p><strong>CVC:</strong> ${document.querySelector('input[name="card_cvc"]').value}</p>
            `;
        } else if (method === 'Bank Transfer') {
            html = `
                <p><strong>Bank Name:</strong> ${document.querySelector('input[name="bank_name"]').value}</p>
                <p><strong>Account Number:</strong> ${document.querySelector('input[name="account_number"]').value}</p>
            `;
        } else if (method === 'Mortgage') {
            html = `
                <p><strong>Mortgage Lender:</strong> ${document.querySelector('input[name="mortgage_lender"]').value}</p>
                <p><strong>Agreement Reference:</strong> ${document.querySelector('input[name="agreement_ref"]').value}</p>
            `;
        }
        return html;
    }

    window.nextStep = function(index) {
        showStep(index);
    };

    document.querySelectorAll(".finalize-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const offerId = btn.dataset.offerId;
            form.action = `/accounts/profile/finalize_offer/${offerId}/`;

            modal.style.display = "flex";
            showStep(1);
        });
    });

    closeBtn.onclick = () => {
        modal.style.display = "none";
    };

    window.onclick = (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };

    const paymentSelect = document.getElementById('id_paymentMethod');
    if (paymentSelect) {
        paymentSelect.addEventListener('change', function () {
            const method = this.value;
            document.getElementById('creditCardFields').style.display = (method === 'Credit Card') ? 'block' : 'none';
            document.getElementById('bankFields').style.display = (method === 'Bank Transfer') ? 'block' : 'none';
            document.getElementById('mortgageFields').style.display = (method === 'Mortgage') ? 'block' : 'none';
        });
    }
});
