// Javascript that Does a refresh using async and await functions, as well as preventing the user from using the back button to 'cheat'

// Event Listener that makes sure the code in the function only starts till everything else is loaded on the page
document.addEventListener("DOMContentLoaded", () =>
{

    // Selects all <a> elements from the game.html page amd stores it in the variable
    const choiceLinks = document.querySelectorAll("a[data-choice]");

    // loops through each of the choices from the models
    choiceLinks.forEach(link =>
    {

        // Event Listener that runs whenever the user clicks on one of the choices
        // When that happens, the line of code goes into effect
        link.addEventListener("click", async (e) =>
        {
            e.preventDefault(); // Stops the normal use of the link for the choices

            const jumpUrl = link.getAttribute("href"); // Stores target URL in a variable

            try
            {
                // Does the async request from earlier
                await fetch(jumpUrl, { method: 'GET' });

                // Prevents the back button being used to go back to a specific scenario
                window.location.replace(jumpUrl);

            }

            catch (error)
            {
                console.error("Navigation error:", error);
            }
        });
    });
});


