# Floodfill kata, response to https://github.com/davidwhitney/CodeDojos/tree/master/FloodFill
# 24/04/20 - Phil Calvert
# Floodfill Class

# You will accept two numbers, w and h, separated by a space.
# You will then accept a grid of ASCII characters of size w*h.
# You will accept two numbers, x and y, and a character c.

class FloodFill:
    def mapper(self, grid, xstart, ystart, replacement_char ):
        accepted_characters = "asdfghjklqwertyuiopzxcvbnmASDFGHJKLQWERTYOPZXCVBNM1234567890@,"

        if replacement_char not in accepted_characters: return "Please supply a valid character"

        w = len(grid[0])
        h = len(grid)

        grid_to_review = grid

        for line in range(len(grid_to_review)):
            grid_to_review[line] = list(grid_to_review[line])

        detected_char = grid_to_review[ystart][xstart]

        coords_to_update = [[xstart,ystart]]
        coords_already_checked = [[xstart,ystart]]

        candidate_coords = [[xstart+1,ystart],[xstart-1,ystart],[xstart,ystart+1],[xstart,ystart-1]]
        
        coords_left_to_check = True
        while coords_left_to_check:
            coords_left_to_check = False
            candidate_coords_buffer = []
            for candidate_coord in candidate_coords:
                if candidate_coord not in coords_already_checked:
                    coords_already_checked.append(candidate_coord)
                    x_to_validate = candidate_coord[0]
                    y_to_validate = candidate_coord[1]

                    # Check coords are in range
                    if x_to_validate >= 0 and x_to_validate < w and y_to_validate >= 0 and y_to_validate < h:
                        if grid_to_review[y_to_validate][x_to_validate] is detected_char:
                            print("Checking coords", x_to_validate, y_to_validate, "should be valid")
                            coords_to_update.append([x_to_validate,y_to_validate])
                            candidate_coords_buffer.append([x_to_validate + 1, y_to_validate])
                            candidate_coords_buffer.append([x_to_validate - 1, y_to_validate])
                            candidate_coords_buffer.append([x_to_validate, y_to_validate + 1])
                            candidate_coords_buffer.append([x_to_validate, y_to_validate - 1])
                            coords_left_to_check = True
                             
                            
                    # If coords are out of range
                    else: 
                        print("Coords", x_to_validate, y_to_validate, " are not valid")

            candidate_coords = candidate_coords_buffer

 
        for i in range(len(coords_to_update)):
            x_to_update = coords_to_update[i][0]
            y_to_update = coords_to_update[i][1]
            grid_to_review[y_to_update][x_to_update] = replacement_char

        for line in range(len(grid_to_review)):
            line_to_insert = "".join(grid_to_review[line])
            grid_to_review[line] = line_to_insert

        return grid_to_review
