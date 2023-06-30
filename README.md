## Explications

**Composition**

La composition est le fait d'avoir une instance d'une classe à l'intérieur d'une autre classe, ce qui permet aux deux classes d'interagir entre elles.

*Exemple dans le code*

Dans [Engine.py](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Engine.py#L22), on utilise une instance de `PasswordGenerator.py` dans le run

---------------

**Encapsulation**

L'encapsulation consiste à restreindre l'accès à certains éléments d'une classe, permettant ainsi de rendre accessibles uniquement les éléments nécessaires à son utilisation.

Pour cela, on utilise la notion de visibilité pour définir l'accès aux propriétés et aux méthodes d'une classe.
- Public: La propriété/méthode sera accessible à l'intérieur mais aussi à l'extérieur de la classe.
- Privé: La propriété/méthode sera accessible uniquement à l'intérieur de la classe.
- Protégé: La propriété/méthode sera accessible uniquement à l'intérieur de la classe et a ses classes filles (Voir Héritage).

En python, il n'y a pas de mot clé pour définir la visibilité, de plus les propriétés/attributs ne sont pas strictement bloqué par le language. A la place des convention de nommage sont utilisé avec des `_` devant le nom des attributs/méthodes.
- 0 underscore = Visibilité public
- 1 underscore = Visibilité protected
- 2 underscore = Visibilité privé

Pour accéder/modifier des propriété privé/protected d'une classe depuis l'extérieur d'une classe, on utilise des méthodes appelé Accesseurs (Getter) et Mutateur (Setter).

En Python, on utilise des propriétés pour définirs les accesseurs et mutateurs en python. On ajoute les décorateurs `@property` avant le mutateur et `@[attribut].setter` pour les mutateurs.

*Exemple dans le code*

- Public: Dans la classe `Options/ManageElement.py`, la méthode [def elements(self, value)](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Options/ManageElement.py#L22) est une méthode public, servant de mutateur a la propriété `_element`

- Protected: Dans la classe `Options/Leet/ManageLeet.py`, la méthode [_run(self)](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Options/Leet/ManageLeet.py#L8) est protected.

- Private: Dans la classe `Engine.py`, la méthode [__init_config(self)](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Engine.py#L58) est privée.

---------------
## Méthodes/attributs statiques, d'objet et de classe

- Les méthode/attributs d'objet est lié à une instance spécifique d'une classe. Elles peuvent accéder aux attributs et aux autres méthodes de cette instance (Utilisation de `self` en python).
- Les méthodes/attributs de classe n'ont pas besoin d'une instance de classe. Elles ne peuvent pas accéder à l'instance `self`, mais elles ont accès à la classe elle-même via `cls`.
- Les méthodes/attributs statiques n'ont pas accès à `cls` ou `self`. Elles fonctionnent comme des fonctions normales, mais elles appartiennent à l'espace de noms de la classe.

En python, on utilise les décorateur `@staticmethod` et `@classmethod` pour définir les méthodes static et de classes. De plus une méthode d'objet a en paramètre par défaut `self`, une méthode de classe a `cls` et static n'en a pas

*Exemple dans le code*

- Objet: Dans la classe `Engine`, la méthodes [get_all_elements](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Engine.py#L27)

- Classe: Dans la classe `Options/ManageElement.py`, la méthode [add_word_possibility(cls, elements=[])](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Options/ManageElement.py#L12) est une méthode de classe. Elle est utilisé dans la classe [Engine.py](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Engine.py#L34).

- Static: Dans la classe `Options/Dates/HumanMonth.py`, la méthode [available_languages(cls)](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/main/back/Classes/Options/Dates/HumanMonth.py#L59) est static. Elle est utilisé dans la classe [Engine.py](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Engine.py#L67)

---------------

## Héritage

L'héritage permet à une classe (appelée classe fille) d'hériter des caractéristiques et du comportement d'une autre classe (appelée classe mère). La classe fille a donc accès a toute les méthodes/attribut public et protected de sa classe mère.

*Exemple dans le code*

La classe [Options/Leet/ManageLeet.py](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Options/Leet/ManageLeet.py) hérite de ma classe abstraite [Options/ManageElement.py](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Options/ManageElement.py), elle est aussi la classe mère de [Options/Leet/LeetMin.py](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Options/Leet/LeetMin.py) et de [Options/Leet/LeetMin.py](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Options/Leet/LeetMax.py)

---------------

## Polymorphisme & Surcharge

Le polymorphisme consiste a redéfinir une méthode en gardant la même signature (Nom, Paramètres, Visibilité et Type de retour), elle est notamment utilisé dans des classes filles, ou lors de l'implémentation de méthode abstraite d'une interface/classe abstraite.
La surcharge quand a elle, consiste a changer la signature d'une méthode en changeant les paramètres (nombres, type et/ou ordre) et en gardant le même nom. Contrairement au polymorphisme, elle n'as pas besoin d'être dans une classe héritée.

*Exemple dans le code*

Dans la classe [Options/Case/Accentless.py](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Options/Case/Accentless.py#L8), la méthode `_run(self)` est un polymorphisme du run de la classe mère `Options/ManageElement.py`

---------------

**Interface et Classe Abstraite**

Une classe abstraite est une classe dont toutes les méthodes n’ont pas été implémentées, elle n’est donc pas instanciable. Une classe qui hérite d’une classe abstraite doit obligatoirement implémenter les méthodes manquantes (déclarées « abstraites » dans la classe parente).

Une interface est un contrat, qui défini un ensemble de comportement que les classes qui l'implémentent. Elle a une collection de méthodes abstraites. Contrairement a la classe abstraite, une classe peut avoir plusieurs interfaces (Alors qu'une classe ne peut hérité que d'une seule classe abstraite) et les interfaces ne peuvent pas avoir de méthodes déjà implémenté.

En python, le module `abc` (Abstract Base Classes) permet de définir des classes abstraite en définissant des méthodes abstraite a l'aide du décorateur `@abstractmethod`. Cependant, il n'y a pas de support intégré pour les interfaces et elles sont simulés en définissant des classes abstraite avec uniquement des méthodes abstraites.

*Exemple dans le code*

La classe [Options/ManageElement.py](https://github.com/ArthurJeannot/MDS-PasswordGuesser-M1/blob/4c9f5418ecad929d37a8f0f88d0de8e19f5d4a6a/back/Classes/Options/ManageElement.py) est une classe abstraite qui est utilisé pour toutes les classes dans les dossier de `/Options/`.
Elle comporte une méthode abstraite `_run(self)` qui doit être implémenté dans toutes les classes filles. Son constructeur, des attributs et des getter/setter sont défini, donc il ne s'agit pas d'une interface.

Si on essaie de l'instancié au lieu d'utilisé ses classes filles, on recoit l'erreur: `TypeError: Can't instantiate abstract class ManageElement with abstract method _run`