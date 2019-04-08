import pygame
from random import *
import bfs
from collections import defaultdict
pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
green=(0,255,0)


gameDisplay=pygame.display.set_mode((400,500))
pygame.display.set_caption('maze runner')
clock=pygame.time.Clock()
crashed=False
w=0
u=0
cx=w+12.5
cy=u+12.5
blocks=[]
blocks.append(1)
for i in range(1,256,1):
    blocks.append(0)
l=0               
for i in range(0,16):
    for j in range(0,16):    
        print(blocks[l],end=' ')
        l+=1
    print(end="\n")  


class block:
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y
        self.nodes=set()
    def add_nodes(self,s):
        self.nodes.add(s)
        
        
bl=[]
ct=0
cy=12.5
for i in range(0,16):
    cx=12.5
    for j in range(0,16):
        bl.append(block(ct,cx,cy))
        ct=ct+1
        cx=cx+25
        
    cy= cy+25


 
 
def genrate():
    oblock=[]
    zblock=[]
    for i in range(0,256):
        if(blocks[i]==0):
            zblock.append(i)
    oblock.append(0)
    oct=1
    zct=255
    
    while(oct!=256):
        ngb=[]
        k=0
        c=choice(oblock)
        
        for i in range(0,zct):
            if((c+1==zblock[i] and c%15!=0)or(zblock[i]==c+1 and c==0)):#rightside
                ngb.append(zblock[i])
                k=k+1
                
                
               
            if(zblock[i]==c-1 and c!=0 and c%16!=0):#leftside
                ngb.append(zblock[i])
                k=k+1
                
                
                
                
            if(zblock[i]==c+16 and c<240):#below
                
                ngb.append(zblock[i])
                k=k+1
                
                
                
                
            if(zblock[i]==c-16 and c>15):#above
                ngb.append(zblock[i])
                k=k+1
                
               
        if(k>0):
            
            print(ngb)   
            d=choice(ngb)
            zblock.remove(d)
        
            if((c+1==d and c%15!=0)or(d==c+1 and c==0)):#right neighbour
                oblock.append(d)
                pygame.draw.line(gameDisplay,black,(bl[c].x+12.5,bl[c].y-12.5),(bl[c].x+12.5,bl[c].y+12.5),5)
                #pygame.draw.line(gameDisplay,red,(bl[c].x,bl[c].y),(bl[d].x,bl[d].y))
                bl[c].add_nodes(d)
            if(c-1==d and c!=0 and c%16!=0):#left neighbour
                oblock.append(d)
                bl[c].add_nodes(d)
                pygame.draw.line(gameDisplay,black,(bl[c].x-12.5,bl[c].y-12.5),(bl[c].x-12.5,bl[c].y+12.5),5)
            if(c-16==d and c>15):#above neighbour
                oblock.append(d)
                bl[c].add_nodes(d)
                pygame.draw.line(gameDisplay,black,(bl[c].x-12.5,bl[c].y-12.5),(bl[c].x+12.5,bl[c].y-12.5),5)
            if(c+16==d and c<240):#below neighbour
                oblock.append(d)
                bl[c].add_nodes(d)
                pygame.draw.line(gameDisplay,black,(bl[c].x-12.5,bl[c].y+12.5),(bl[c].x+12.5,bl[c].y+12.5),5)
            
                
               
            zct=zct-1
            oct=oct+1

g=defaultdict(list)            
for i in range(0,256):
    g[i]=bl[i].nodes
    #print(g[i])
                
def text_objects(text,font):
    textSurface= font.render(text,True,black)
    return textSurface,textSurface.get_rect()

                
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    print(click)
    
    if (x+w> mouse[0] > x and y+h > mouse[1] > y ):
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        
        if click==1 and action !=None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        
    smallText=pygame.font.Font("freesansbold.ttf",20)
    textSurf,textRect= text_objects(msg,smallText)
    textRect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)
    
    
    

#buliding grid:        
    
for i in range(0,400,25):
    
    for j in range(0,400,25):
                    
            pygame.draw.line(gameDisplay,white,(i,j),(i,j+25),5)
for j in range(0,425,25):
    for i in range(0,400,25):
            pygame.draw.line(gameDisplay,white,(i,j),(i+25,j),5)
            
pygame.draw.rect(gameDisplay,green,(0,0,25,25))           
pygame.draw.rect(gameDisplay,green,(375,375,25,25))
button("maze",150,425,100,50,red,green,genrate())
#graph
for i in range(0,256):
    g[i]=bl[i].nodes
    print(g[i])
    
print(bfs.bfss(g,0))
p=[]
p=bfs.shortest_path(g,0,255,bl,gameDisplay)
pt=0
pygame.display.update()
while(p[pt]!=255):
    m=p[pt]
    n=p[pt+1]
    pygame.draw.line(gameDisplay,red,(bl[m].x,bl[m].y),(bl[n].x,bl[n].y),3)
    clock.tick(3)
    pygame.display.update()
    pt=pt+1
    
    
    
pygame.display.update() 

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        #print(event)
    
    clock.tick(60)
pygame.quit
quit()