import random
import skills

# hero
class hero:
    name = 'Zetter'
    m_hp = 100 # max hp
    c_hp = 100 # current hp
    att = 10
    arm = 2
    arp = 1
    m_stm = 50 # max stamina
    c_stm = 50 # current stamina
    u_stm = 5 # stamina used
    r_stm = 20 # stamina recovered
    evasion = False
    skills = {heal: [5, 5], fireball: [3, 3], stun: [10, 10]}

# mob
class mob:
    name = 'Weak fly'
    m_hp = 100 # max hp
    c_hp = 100 # current hp
    att = 10
    arm = 3
    arp = 0
    m_stm = 500 # max stamina
    c_stm = 500 # current stamina
    u_stm = 2 # stamina used
    r_stm = 10 # stamina recovered
    evasion = False

#def damage(attacker, defender):
#    defender.c_hp = defender.c_hp +  (defender.arm - attacker.arp) - attacker.att

#old        
#def turn():
#    damage(mob, hero)
#    damage(hero, mob)

def attack(attacker, defender):
    '''Attack'''
    if defender.evasion:
        defender.evasion = False
        print(f'{attacker.name} missed {defender.name}')
    else:
        defender.c_hp = defender.c_hp + defender.arm - attacker.arp - attacker.att
        attacker.c_stm -= attacker.u_stm
        print(f'{attacker.name} deal {attacker.att - defender.arm + attacker.arp} damage')

def evade(evader, pc):
    '''Evade'''
    if evader.c_stm >= evader.u_stm * 4:
        evader.evasion = True
        evader.c_stm -= evader.u_stm * 4
        print(f'{evader.name} succesfully evaded')
    else:
        print('{evader.name} cannot evade and loose a turn')

def wait(waiter, pc):
    '''Wait'''
    waiter.c_stm = min(waiter.m_stm, waiter.c_stm + waiter.r_stm)
    print(f'{waiter.name} have recovered {waiter.r_stm} stamina')

def skills(caster, target):
    '''Skills'''
#    target.c_hp -= caster.att * 2
#    print(f'{caster.name} casts fireboll on {target.name} dealing {caster.att * 2} damage')
    skills_menu(caster)

def actions_menu(voc):
    for k, v in voc.items():
    	print(f'{k}: {v.__doc__}')
    	
def skills_menu(voc):
    for k, v in voc.items():
        print(f'{k}, cd: {v[0]}/{v[1]}, {k.__doc__}')

combat_actions = {1: evade, 2: attack, 3: wait, 4: skills }
# attack block? evade?

def effects(): # dot, hot, stun, blind, vuln, might; alac?, quick?, daze?
    '''Effects'''
    print('even \033[96meffects\033[00m o_0')


def turn():
    #info
    print(f'Your stamina {hero.c_stm} / {hero.m_stm}, mob stamina {mob.c_stm} / {mob.m_stm}')
    print(f'Your hp {hero.c_hp} / {hero.m_hp}, mob hp {mob.c_hp} / {mob.m_hp}')
    actions_menu(combat_actions)
    
    p_act = int(input('Choose your des.. i meant action: ')) # hero action
    m_act = random.randint(1,4)
    try:
        if m_act < p_act:
            combat_actions[m_act](mob, hero)
            combat_actions[p_act](hero, mob)
        else:
            combat_actions[p_act](hero, mob)
            combat_actions[m_act](mob, hero)
        effects()
    except:
        pass
    

#combat
while mob.c_hp > 0 and hero.c_hp > 0:
    turn()
    
if mob.c_hp <= 0 and hero.c_hp <= 0:
    print('Tie')
elif mob.c_hp <= 0:
    print (f'{hero.name} win')
else:
    print (f'{mob.name} loose')
    
# timers
# effects
# skill choose

