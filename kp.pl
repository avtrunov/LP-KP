:- discontiguous(father/2).
:- discontiguous(mother/2).
father(vladimir,anton).
mother(tatiana,anton).
mother(zoya,tatiana).
mother(zoya,olga).
father(alexandr,tatiana).
father(alexandr,olga).
mother(olga,eugeny).
mother(olga,svetlana).
father(viktor,svetlana).
father(eugeny,sofia).
mother(angela,sofia).
father(georgy,eugeny).
father(sergay,irina).
father(sergay,galina).
father(sergay,vladimir).
mother(maria,irina).
mother(maria,galina).
mother(maria,vladimir).
mother(irina,vadim).
mother(galina,inna).
father(semion,vadim).
father(valery,inna).

husband(X,Y):-
	father(X,Z),
	mother(Y,Z),
	X \= Y.
wife(X,Y):-
	husband(Y,X).
female(X):-
	mother(X,Y).
child(X,Y):-
	mother(Y,X);father(Y,X),
	X \= Y.
sibling(X,Y):-
	child(X,Z),
	child(Y,Z),
	X \= Y.
zolovka(X,Y):-
	female(X),
	sibling(X,Z),
	wife(Y,Z),
	X \= Y.
