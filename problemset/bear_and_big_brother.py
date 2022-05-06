limak, bob = input().split()
m_limak = int( limak )
m_bob = int( bob )
years = 0
while True :
    years += 1
    m_limak = m_limak * 3 
    m_bob = m_bob * 2
    if m_limak > m_bob :
        break

print( years )
            
