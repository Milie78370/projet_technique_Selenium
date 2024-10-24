Feature: Test partie de la connexion à l'application

    Scenario Outline: Formulaire email
      Given J'accede à la page onboarding de dilitrust
      When Je saisie un "<email>" valide
      And Je clique sur le bouton validation
      Then Je vois "<result>"
      Examples:
        | email           | result                                    |
        | test@gmail.com  | Le reste du formulaire apparaît           |
        | test            | Invalid mail                              |

    #Deuxieme scénario pour tester la connexion
    """Scenario Outline: Formulaire connexion
      Given J'accede à la page onboarding de dilitrust
      When Je saisie un "<email>" valide
      And Je clique sur le bouton validation
      And Je saisie un "<password>"
      And Je clique sur le bouton validation
      Then J'arrive sur "<page>"
      Examples:
        | email          | password   | page          |
        | test@gmail.com |  azerty    | onboarding    |
        | test@gmail.com |  a         | collaborateur |"""
