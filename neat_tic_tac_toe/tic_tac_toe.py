import neat
import os 
import sys

tic_tac_toe_inputs = []
tic_tac_toe_outputs = []

with open("all_tic_tac_toe", "r") as f:
    x = f.readlines()
    for i in x:
        temp = i.split(',')[0]
        x = [int(j) for j in temp]
        # print(x)
        print(len(x))
        tic_tac_toe_inputs.append(x)
        tic_tac_toe_outputs.append(int(i[1][0]))


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 4.0
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        for xi, xo in zip(tic_tac_toe_inputs, tic_tac_toe_outputs):
            output = net.activate(xi)
            genome.fitness -= (output[0]-xo) ** 2


def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    winner = p.run(eval_genomes, 300)
    print("\nBest genome: \n{!s}".format(winner))
    

    print("\n Output: ")
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    for xi, xo in zip(tic_tac_toe_inputs, tic_tac_toe_outputs):
        output = winner_net.activate(xi)
        print("input {!r} expected output {!r}, got {!r}".format(xi, xo, output))


    p.run(eval_genomes, 10)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    run(config_path)
