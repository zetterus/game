def heal(healer, target):
'''Heal target for 1/5 of your max hp'''
    target.c_hp = min(target.c_hp + int(healer.m_hp / 5), target.m_hp)
    print(f'{target.name} healed for {min(target.c_hp + int(healer.m_hp / 4), target.m_hp)}')
