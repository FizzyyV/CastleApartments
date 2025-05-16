document.addEventListener('DOMContentLoaded', function(){
    function registerSearchButtonHandler(){
        const SearchButton = document.getElementById('SearchButton')
        SearchButton.addEventListener("click", async function(){
            const searchValueElementS= document.getElementById("Street");
            const searchValueElementPO = document.getElementById("PostalCode");
            const SearchValueElementT = document.getElementById("Type");
            const SearchValueElementPR = document.getElementById("PriceRange");
            const SearchValueElementO = document.getElementById("OrderedBy");
            const propertyDisplayer = document.getElementById('property-displayer');
            const StreetValue = searchValueElementS.value;
            const TypeValue = SearchValueElementT.value;
            const PriceRangeValue = SearchValueElementPR.value;
            const OrderedByValue = SearchValueElementO.value;
            const PostalCodeValue = searchValueElementPO.value;


            const responce = await fetch(`?street_filter=${StreetValue}&postal_filter=${PostalCodeValue}&type_filter=${TypeValue}&price_filter=${PriceRangeValue}&order_filter=${OrderedByValue}`);
            if (responce.ok){
                const json = await responce.json();
                const properties = json.data.map(property => `
                   <div class="property-item">
                   <a href="${property.id}" class="property-link">
                        <div class="property-image-container">
                        <div class="property-image" style="background-image: url(${ property.propThumbnail})"></div>
                        </div>
                        <div class="property-info">
                            <h3>${property.propertyName} ${property.house_number}</h3>
                            <p>${property.city} ${property.postal_code}</p>

                            <div class="price-size">
                                <div class="price">Price: ${property.propListingPrice}</div>
                                <div class="size">${property.propSquareMeters} m2</div>
                            </div>

                            <div class="details">
                                <span>${property.propBedrooms} Bedrooms</span>
                                <span>${property.propBathrooms} Bathroom</span>
                            </div>

                            <div class="built-year">Built ${property.built}</div>
                        </div>
                    </div>
                `);
                propertyDisplayer.innerHTML = properties.join('')

                console.log(json);
            }
        })
    }
    registerSearchButtonHandler();
});