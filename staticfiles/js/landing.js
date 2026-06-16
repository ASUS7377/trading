// Карусель отзывов

const reviews = document.querySelectorAll('.review');

let currentReview = 0;

function showReview(index){

    reviews.forEach((review)=>{

        review.classList.remove(
            'active'
        );

    });

    reviews[index].classList.add(
        'active'
    );

}

if(reviews.length > 0){

    setInterval(()=>{

        currentReview++;

        if(
            currentReview >=
            reviews.length
        ){

            currentReview = 0;

        }

        showReview(
            currentReview
        );

    },5000);

}


// Плавное появление блоков

const observer = new IntersectionObserver(

(entries)=>{

    entries.forEach((entry)=>{

        if(
            entry.isIntersecting
        ){

            entry.target.classList.add(
                'show'
            );

        }

    });

},

{
    threshold:0.15
}

);

document
.querySelectorAll(

'.feature-card,.screen-card,.price-card,.review,.cta'

)
.forEach((el)=>{

    el.classList.add(
        'hidden-section'
    );

    observer.observe(
        el
    );

});