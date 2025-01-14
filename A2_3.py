import turtle

def draw_branch(branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:
        return
    else:
        # Draw the current branch
        turtle.forward(branch_length)
 
        turtle.right(right_angle)
        draw_branch(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)

        turtle.left(right_angle + left_angle) 
        draw_branch(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
        
        turtle.right(left_angle)
        turtle.backward(branch_length)

def main():
    left_angle = float(input("Enter the left branch angle (degrees): "))
    right_angle = float(input("Enter the right branch angle (degrees): "))
    starting_length = float(input("Enter the starting branch length (pixels): "))
    recursion_depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7 for 70%): "))

    turtle.left(90)
    turtle.up() 
    turtle.backward(100)  
    turtle.down()
    turtle.color("green")

    draw_branch(starting_length, left_angle, right_angle, recursion_depth, reduction_factor)

    turtle.done()

if __name__ == "__main__":
    main()