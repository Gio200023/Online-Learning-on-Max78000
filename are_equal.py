output_channel_0=[-16,44,94,46,-69,-28,12,-7,-107,-69,-11,9,-3,9,11,-1,37,36,11,73,37,-23,14,81,-1,-46,-23,-17,-11,-40,-13,-47,-22,-17,64,82,-11,-10,65,113,1,44,115,126,41,74,126,104,17,2,-11,-28,-14,-72,-74,-45,-53,-116,-124,-34,-8,-69,-75,-25,70,40,-11,-46,41,19,-120,-115,35,30,-118,-122,23,13,-80,-73,40,89,104,40,62,106,109,-15,52,119,75,-28,52,73,37,0,12,13,33,8,-15,-9,-10,-54,-60,-96,-74,-71,-15,-56,-47,-26,4,82,112,94,-89,-22,124,125,-126,-126,73,101,-114,-83,69,69,8,-37,-34,17,45,-17,-49,5,5,-6,-29,17,-16,-77,-84,-23,-29,-42,-35,13,-42,-54,-56,-12,-14,-32,23,78,-34,1,94,115,0,6,5,-9,-48,-57,-36,-38,-58,-57,-23,-45,-33,-42,2,10,-23,9,60,4,-28,1,32,-34,-45,-50,-28,-42,-47,-63,-13,-14]

Kernels_layer4_firstline_mod2=[-16,44,94,46,-69,-28,12,-7,-107,-69,-11,9,-3,9,11,-1,37,36,11,73,37,-23,14,81,-1,-46,-23,-17,-11,-40,-13,-47,-22,-17,64,82,-11,-10,65,113,1,44,115,126,41,74,126,104,17,2,-11,-28,-14,-72,-74,-45,-53,-116,-124,-34,-8,-69,-75,-25,70,40,-11,-46,41,19,-120,-115,35,30,-118,-122,23,13,-80,-73,40,89,104,40,62,106,109,-15,52,119,75,-28,52,73,37,0,12,13,33,8,-15,-9,-10,-54,-60,-96,-74,-71,-15,-56,-47,-26,4,82,112,94,-89,-22,124,125,-126,-126,73,101,-114,-83,69,69,8,-37,-34,17,45,-17,-49,5,5,-6,-29,17,-16,-77,-84,-23,-29,-42,-35,13,-42,-54,-56,-12,-14,-32,23,78,-34,1,94,115,0,6,5,-9,-48,-57,-36,-38,-58,-57,-23,-45,-33,-42,2,10,-23,9,60,4,-28,1,32,-34,-45,-50,-28,-42,-47,-63,-13,-14]

def areEqual(arr1,arr2,n,m):
    #Iflengthsofarrayarenot
    # equal means arrays are not equal
    if (n != m):
        return False
 
    # Sort both arrays
    arr1.sort()
    arr2.sort()
    
    print(arr1)
    print(arr2)
 
    # Linearly compare elements
    for i in range(0, n):
        if (arr1[i] != arr2[i]):
            return False
 
    # If all elements were same.
    return True

def oneEqual(arr1,arr2,n,m):
    for h in range(len(arr1)):
        for m in range(len(arr2)):
            if arr1[h] == arr2[m]:
                print(arr1[h],end=',')
        
    
 
n = len(output_channel_0)
m = len(Kernels_layer4_firstline_mod2)

# print(n)
# print(m)

if (areEqual(Kernels_layer4_firstline_mod2, output_channel_0, n, m)):
    print("Yes")
else:
    print("No")

