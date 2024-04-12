document.getElementById('searchForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const search1 = document.getElementById('search1').value;
    const search2 = document.getElementById('search2').value;
    alert(`Recherche 1 : ${search1}\nRecherche 2 : ${search2}`);
    // Vous pouvez ajouter ici le code pour effectuer la recherche
});

document.getElementById('searchButton2').addEventListener('click', function () {
    const search2 = document.getElementById('search2').value;
    alert(`Recherche 2 : ${search2}`);
    // Vous pouvez ajouter ici le code pour effectuer la recherche du deuxième formulaire
});