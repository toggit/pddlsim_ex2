
(define (problem attack_agent)
(:domain attack)
(:objects
	attacker1
	win10_1
	win10_2
	win10_3
	win7_1
	win7_2
	win7_3
	ubuntu16_1
	ubuntu16_2
	ubuntu16_3
	linux_mint_1
	)
(:init
	(attacker attacker1)
	(ubuntu16 ubuntu16_1)
	(ubuntu16 ubuntu16_2)
	(ubuntu16 ubuntu16_3)
	(win10 win10_1)
	(win10 win10_2)
	(win10 win10_3)
	(win7 win7_1)
	(win7 win7_2)
	(win7 win7_3)
	(linux_mint linux_mint_1)
	(controlled attacker1 win10_1)
	(connected win10_1 win10_2)
	(connected win10_2 win10_3)
	(connected win10_3 win7_1)
	(connected win7_1 win7_2)
	(connected win7_2 win7_3)
	(connected win7_3 ubuntu16_1)
	(connected ubuntu16_1 ubuntu16_2)
	(connected ubuntu16_2 ubuntu16_3)
	(connected ubuntu16_3 linux_mint_1)
    )
(:goal 
    (and (controlled attacker1 linux_mint_1))
	)
)
