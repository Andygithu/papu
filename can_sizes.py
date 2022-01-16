import math
 
def main():
 
     cans_name = ["#1 Picnic",  "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
     cans_radius = [ 6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.4, 6.83, 15.72, 6.83, 7.62, 8.1 ]    
     cans_height = [ 10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
     cans_cost = [0.28,  0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42] 
 
     for i in range(12):
        volume = compute_volume(cans_radius[i], cans_height[i])
        surface = compute_surface(cans_radius[i], cans_height[i])
        storage_efficiency = compute_storage_efficiency(volume, surface)
        
 
        # print(f"{cans_name[i]}, Volume: {volume:.2f}, Surface: {surface:.2f}, {storage_efficiency:.1f}")
        print(f"{cans_name[i]}  {storage_efficiency:.1f}")

        
        # print(f"{cans_name[i]},{cans_radius[i]}, {cans_height[i]}, {cans_cost[i]}")




def compute_volume(cans_radius, cans_height):
   cans_volumne = math.pi * cans_radius ** 2 * cans_height
   return cans_volumne
 
def compute_surface(cans_radius, cans_height):
   cans_surface = 2 * math.pi * cans_radius * (cans_radius + cans_height)
   return cans_surface

def compute_storage_efficiency(volume, surface_area):
     storage_efficiency = volume / surface_area
     return storage_efficiency

main()