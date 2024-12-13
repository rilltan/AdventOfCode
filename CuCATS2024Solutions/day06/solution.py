
import png # https://pypng.readthedocs.io/en/latest/
import os

SHARD_WIDTH = 112
SHARD_HEIGHT = 64

X_SHARDS = 16
Y_SHARDS = 16

class Shard:
    def __init__(self, width, height, pixels, filename):
        self.width = width
        self.height = height
        self.pixels = pixels
        self.filename = filename
    
    def build_edges(self,edge_no):
        if edge_no==0:
            return [x for x in self.pixels[0]]
        elif edge_no==1:
            return [(x[-2]+x[-3]+x[-1]) for x in self.pixels]
        elif edge_no==2:
            return [x for x in self.pixels[-1]]
        elif edge_no==3:
            return [(x[0]+x[1]+x[2]) for x in self.pixels]
        else:
            raise Exception
    
    def compare_to_opposite_edge(self, edge_no, other):
        other_edge = other.build_edges((edge_no+2)%4)
        our_edge = self.build_edges(edge_no)
        return sum([abs(our_edge[i]-other_edge[i]) for i in range(len(other_edge))])

def build_image(shards : list[Shard]):
    out = []
    for y in range(Y_SHARDS):
        for ya in range(SHARD_HEIGHT):
            out.append([])
            for x in range(X_SHARDS):
                out[y*SHARD_HEIGHT+ya].extend(shards[y*X_SHARDS+x].pixels[ya])
    return out

def main():
    files = os.listdir("CuCATS2024Solutions/day06/chunks")
    shards = []
    for filename in files:
        reader = png.Reader(filename=f"CuCATS2024Solutions/day06/chunks/{filename}")
        width, height, pixels, metadata = reader.read()
        shard = Shard(width, height, list(pixels), filename)
        shards.append(shard)
    
    # TODO:
    # - calculate 4 * n^2 shard connection scores, for every pair of shards and every edge
    # - match shards together greedily with highest scores
    # - output the stitched image
    # print(shards[115].compare_to_opposite_edge(2,shards[166]))
    # print(shards[115].compare_to_opposite_edge(2,shards[167]))
    #print([x[-3] for x in shards[0].pixels])
    hor_scores = {}
    ver_scores = {}
    for i in range(X_SHARDS*Y_SHARDS):
        for j in range(X_SHARDS*Y_SHARDS):
            if i==j:
                continue
            if i not in hor_scores:
                hor_scores[i] = {k:9999999999 for k in range(X_SHARDS*Y_SHARDS)}
            if i not in ver_scores:
                ver_scores[i] = {k:9999999999 for k in range(X_SHARDS*Y_SHARDS)}
            top_score = shards[i].compare_to_opposite_edge(0,shards[j])
            left_score = shards[i].compare_to_opposite_edge(3,shards[j])
            if i==97 and j == 115:
                print(left_score)
            hor_scores[i][j] = top_score
            ver_scores[i][j] = left_score
    # print(ver_scores[97])
    # print(sorted([a for a in range(X_SHARDS*Y_SHARDS) if a!=(0)],key=ver_scores[97].get)[0])
    start = shards[-9]
    new_shards = [0] * (X_SHARDS*Y_SHARDS)
    new_shards[-1] = start
    new_shards_indices = [-1] * (X_SHARDS*Y_SHARDS)
    new_shards_indices[-1] = 256-9
    for y in range(Y_SHARDS-1,-1,-1):
        for x in range(X_SHARDS-1,0,-1):
            #print(y*X_SHARDS+x-1)
            #print(sorted([a for a in range(X_SHARDS*Y_SHARDS) if a!=(y*X_SHARDS+x)],key=ver_scores[y*X_SHARDS+x].get)[0])
            if y==15:
                new_shards_indices[y*X_SHARDS+x-1] = sorted([a for a in range(256) ],key=ver_scores[new_shards_indices[y*X_SHARDS+x]].get)[0]
            else:
                b=0
                hor_list = sorted([a for a in range(256) ],key=hor_scores[new_shards_indices[(y+1)*X_SHARDS+x-1]].get)
                if y*X_SHARDS+x-1==117:
                    print(hor_list)
                while hor_list[b] in new_shards_indices or (y*X_SHARDS+x-1 == 101 and hor_list[b]==196 ) or (y*X_SHARDS+x-1 == 87 and hor_list[b]==8 ):
                    b+=1
                new_shards_indices[y*X_SHARDS+x-1] = hor_list[b]
                if (y*X_SHARDS+x-1 == 87):
                    new_shards_indices[y*X_SHARDS+x-1] = 196
            #     ver_list = sorted([a for a in range(X_SHARDS*Y_SHARDS) if a!=(new_shards_indices[y*X_SHARDS+x])],key=ver_scores[new_shards_indices[y*X_SHARDS+x]].get)
            #     new_shards_indices[y*X_SHARDS+x-1] = sorted([c for c in range(X_SHARDS*Y_SHARDS) if c!=new_shards_indices[(y+1)*X_SHARDS+x-1] and c!=new_shards_indices[y*X_SHARDS+x]],key = lambda d: hor_list.index(d)+ver_list.index(d))[0]
            new_shards[y*X_SHARDS+x-1] = shards[new_shards_indices[y*X_SHARDS+x-1]]
        new_shards_indices[y*X_SHARDS-1]=sorted([a for a in range(X_SHARDS*Y_SHARDS) if a!=(new_shards_indices[(y+1)*X_SHARDS-1])],key=hor_scores[new_shards_indices[(y+1)*X_SHARDS-1]].get)[0]
        new_shards[y*X_SHARDS-1] = shards[new_shards_indices[y*X_SHARDS-1]]
    
    writer = png.Writer(SHARD_WIDTH*X_SHARDS,SHARD_HEIGHT*Y_SHARDS,bitdepth=8,greyscale=False)
    with open("CuCATS2024Solutions/day06/out.png","wb") as f:
        writer.write(f,build_image(new_shards))
    with open("CuCATS2024Solutions/day06/out1.png","wb") as f:
        writer.write(f,build_image(shards))



if __name__ == "__main__":
    main()

