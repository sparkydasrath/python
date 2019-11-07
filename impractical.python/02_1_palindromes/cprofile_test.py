import cProfile
import palingram
import palingram_optimized

# cProfile.run("palingram.find_palingrams()")

cProfile.run("palingram_optimized.find_palingrams_opt()")

