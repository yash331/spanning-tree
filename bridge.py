class Lan:
    
    def __init__(self,name):
        self.name=name
        #(list of [bridge name,distance,root bridge])
        self.message=[]

    def clear_message(self):
        self.message=[]

class Bridge:

    def __init__(self,name,lan):
        self.name=name
        self.lan=lan
        #[bridge name,distance, root bridge]
        self.send=[name,0,name]
        self.port={}
        self.previousid=name

        for a1 in lan:      #(self.lan?)
            #{lan_name:bridge_name,current state} first all are DP
            self.port[a1.name]=[self.name,"DP"] 

    def determine_sending_message(self):        
        optimum_message={}
        for a5 in self.lan:     #t print meassages from lan at a bridge
            if self.port[a5.name][1]!="NP":
                messages=[]
                for a6 in a5.message:
                    x=[a6[2],a6[1],a6[0]]   #root bridge, distance, brdige
                    messages.append(x)

                if len(messages)==0:    #lan is empty
                    return

                optimum_message[a5.name]=min(messages)  #i=[1,2,3], j=[1,3,5], k=[2,4,1], l=[2,3,5], d=[i,j,k,l]=i

        sorted_optimum_messages=sorted(optimum_message.items(),key=lambda x:x[1])

        if sorted_optimum_messages[0][1][2]!=self.name:
            self.send[2]=sorted_optimum_messages[0][1][0]   #again chaning order this is root bridge name
            self.send[1]=sorted_optimum_messages[0][1][1]+1 #distance increment 
            self.send[0]=self.name  #bridge name
            self.port[sorted_optimum_messages[0][0]][1]="RP"    #because root is in that direction
            

        for a5 in sorted_optimum_messages:
            if a5[1][0]==self.send[2] and a5[1][2]!=self.name and self.port[a5[0]][1]!="RP":
                self.port[a5[0]][1]="NP"

        npwnp=0;
        lan_name=None
        for a1 in self.lan:
            if self.port[a1.name][1]!="NP":
                lan_name=a1.name
                npwnp+=1

        if npwnp==1:
            self.port[lan_name][1]="NP"

        


        return


    def sending_message(self):
        for a1 in self.lan:
            if self.port[a1.name][1]=="DP":
                a1.message.append(self.send)