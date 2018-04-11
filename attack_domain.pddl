(define (domain attack)
(:predicates
	 (controlled ?p ?x) (attacker ?p) (ubuntu16 ?x) (win10 ?x) (win7 ?x) (linux_mint ?x) (connected ?a ?b))

(:action attack-win10
 :parameters ( ?p ?a ?b)
 :precondition
	(and (attacker ?p) (win10 ?b) (controlled ?p ?a) (connected ?a ?b))
 :effect
	(and (controlled ?p ?b)))
	
(:action attack-win7
 :parameters ( ?p ?a ?b)
 :precondition
	(and (attacker ?p) (win7 ?b) (controlled ?p ?a) (connected ?a ?b)) 
 :effect
	(and (controlled ?p ?b)))
	
(:action attack-ubuntu16
 :parameters ( ?p ?a ?b)
 :precondition
	(and (attacker ?p) (ubuntu16 ?b) (controlled ?p ?a) (connected ?a ?b))
 :effect
	(and (controlled ?p ?b)))
	
(:action attack-linux_mint
 :parameters ( ?p ?a ?b)
 :precondition
	(and (attacker ?p) (linux_mint ?b) (controlled ?p ?a) (connected ?a ?b))
 :effect
	(and (controlled ?p ?b)))
)
