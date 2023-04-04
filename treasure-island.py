print('''
*******************************************************************************
          ( )___( )
          /__oo   \
         ( \/     )
         | `=/    |
        /         \
       /  /    \   \
      /  (      \   \
     ( ,_/_      \   \
      \_ '=       \   )
        ""'       /  /
        ;        /  /'?
        :       (((( /
   ctr   `._   \  _ (
          __|   |  /_
        ("__,.."'_._.)
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

command = input("Left or Right?")
if command.lower() == 'left':
    command = input("Swim or Wait?")
    if command.lower() == 'wait':
        command = input("Which door? Blue? Red? Yellow?")
        if command.lower() == 'yellow':
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")
