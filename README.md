# 3D-tetoris
3Dのテトリスです。this is 3D tetoris.

操作方法:  (def move_state()に記載)
 if event.key==pygame.K_RIGHT: right=True #右進行  
 if event.key==pygame.K_LEFT: left=True #左進行   
 if event.key==pygame.K_m: oku=True #奥進行  
 if event.key==pygame.K_n: temae=True #手前進行  
 
 if event.key==pygame.K_DOWN: down=True #下進行    
 if event.key==pygame.K_UP: drop=True #急落下  
 if event.key==pygame.K_f: p_rotate=True #右回転    
 if event.key==pygame.K_d: m_rotate=True #左回転   
 if event.key==pygame.K_s: p_rotate_oku=True #奥右回転    
 if event.key==pygame.K_a: m_rotate_oku=True #奥左回転   
