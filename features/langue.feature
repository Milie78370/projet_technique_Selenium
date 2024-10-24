Feature: Choix de langue sur la page
    Scenario Outline: Langue de la page
      Given J'accede à la page dilitrust
      When Je clique sur le bouton Langue
      And Je choisis la "<langue>"
      Then Je suis redirigé vers la page de la "<prefix_lang>"
      Examples:
        | langue | prefix_lang  |
        | 1       | fr          |
        | 4       | it          |