document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); 

    var przedrostek = document.getElementById('przedrostek').value;
    var imie = document.getElementById('imie').value;
    var nazwisko = document.getElementById('nazwisko').value;
    var email = document.getElementById('email').value;
    var telefon = document.getElementById('telefon').value;

    var data = {
      'przedrostek': przedrostek,
      'imie': imie,
      'nazwisko': nazwisko,
      'email': email,
      'telefon': telefon
    };

    fetch('https://xzt9bm6t86.execute-api.eu-central-1.amazonaws.com/dev', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(function(response) {
      if (response.ok) {
        alert("Dane zostały zapisane.");
        document.getElementById('imie').value = "";
        document.getElementById('nazwisko').value = "";
        document.getElementById('email').value = "";
        document.getElementById('telefon').value = "";
      } else {
        alert("Wystąpił błąd. Spróbuj ponownie.");
      }
    })
    .catch(function(error) {
      console.log('Wystąpił błąd:', error.message);
      alert("Wystąpił błąd. Spróbuj ponownie.");
    });
  });