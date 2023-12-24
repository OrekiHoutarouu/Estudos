document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#submit").addEventListener("click", function(){
        let user_game = document.querySelector("#user_game");
        let user_game_description = document.querySelector("#user_game_description");

        let user_game_placeholder = document.querySelector("#user_game_placeholder");
        user_game_placeholder.innerHTML = user_game.value;


        let user_game_description_placeholder = document.querySelector("#user_game_description_placeholder");
        user_game_description_placeholder.innerHTML = user_game_description.value;
    })
})
