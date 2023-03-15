
#armstrong checking

arm=int(input("enter a number check armstrong or not"))
arms=arm
su=0
while arm>0:
    k=arm%10
    su=su+(k*k*k)
    arm=int(arm/10)
if (arms==su):
    print("its armstrong")
else:
    print("not armstrong")