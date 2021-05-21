#pragma GCC optimize("Ofast")
#pragma GCC optimize("inline")
#pragma GCC optimize("omit-frame-pointer")
#pragma GCC optimize("unroll-loops")
#pragma GCC option("arch=native","tune=native","no-zero-upper")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <chrono>

#define WIDTH 7
#define HEIGHT 6
#define MAX_USE_TIME 95
#define DEBUG true

using namespace std::chrono;
using namespace std;

constexpr char copyright[] = "Jrke's Special."; //Don't remove
constexpr int NONE = 0;
constexpr int ME = 1;
constexpr int OPP = 2;
constexpr int TIMES = 4;
constexpr int WEIGHT_LINE = 2;
constexpr int WEIGHT_PLACE = 2;
constexpr int VALID_COUNT = 7;
constexpr int WIN = 1000000;
constexpr int LOOSE = -WIN;
constexpr int DRAW = 0;
constexpr int MAXDEPTH = 9;
constexpr float GAMMA = .99;
constexpr int VALIDS[VALID_COUNT] = {3, 2, 4, 1, 5, 0, 6};
constexpr int DIR[8][2] = {{1, 0}, {1, 1}, {1, -1}, {0, 1}, {0, -1}, {-1, 0}, {-1, 1}, {-1, -1}};

class board {
public:

    int map[WIDTH][HEIGHT];
    int turns;

    inline board () {}
    ~board() {}

    inline void play(const int& move, const int& player) {
        for (int y = 0; y < HEIGHT; y++) {
            if (map[move][y] != 0) {
                map[move][y - 1] = player;
                break;
            }
            if (y == HEIGHT - 1) {
                map[move][y] = player;
            }
        }
        turns += 1;
    }

    inline bool valid(const int& move) {
        return map[move][0] == 0;
    }

    inline int lineLenght(const int& x, const int& y, const int& id) {
        int MAXLEN = -1;
        for (int i = 0; i < 8; i++) {
            int len = 1;
            int a = x + DIR[i][0];
            int b = y + DIR[i][1];
            while (a > -1 && a < WIDTH && b > -1 && b < HEIGHT && map[a][b] == id) {
                len += 1;
                a += DIR[i][0];
                b += DIR[i][1];
            }
            if (len > MAXLEN) MAXLEN = len;
        }
        return MAXLEN;
    }

    inline bool win(const int& id) {
        for (int x = 0; x < WIDTH; x++) {
            for (int y = 0; y < HEIGHT; y++) {
                if (map[x][y] == id) {
                    if (lineLenght(x, y, id) > TIMES - 1) return true;
                }
            }
        }
        return false;
    }

    inline float value(const int& id) {
        float val = 0;
        for (int x = 0; x < WIDTH; x++) {
            for (int y = 0; y < HEIGHT; y++) {
                if (map[x][y] != NONE) {
                    val += lineLenght(x, y, map[x][y]) * (map[x][y] == id?1:-1) * WEIGHT_LINE;
                    val += (WIDTH - (abs(int(WIDTH / 2) - x)) * WEIGHT_PLACE) * (map[x][y] == id?1:-1);
                }            
            }
        }
        return val;
    }
};

inline int minimax(board& connect4, const int& DEPTH, const int& id, const int beta, const bool root) {
    if (DEPTH == 0) return connect4.value(id);
    int oppId = id == ME?OPP:ME;
    int MAXVAL = LOOSE * 10;
    int best = -1;
    board save = connect4;
    for (int m = 0; m < VALID_COUNT; m++) {
        int move = VALIDS[m];
        if (connect4.valid(move)) {
            connect4.play(move, id);
            if (connect4.win(id)) return root?move:WIN;
            int THISVAL = -minimax(connect4, DEPTH - 1, oppId, MAXVAL, false) * GAMMA;
            if (THISVAL > MAXVAL) {
                MAXVAL = THISVAL;
                best = move;
            }
            connect4 = save;
            if (-MAXVAL * GAMMA <= beta && !root) break;
        }
    }
    if (best == -1) return DRAW;
    return root?best:MAXVAL;
}

class state {
public:

    board connect4;
    string sboard;
    int id;
    int COMMAND;

    inline state() {
        COMMAND = 0;
    }
    ~state() {}

    inline void update() {
        cin >> id; cin.ignore();
        cin >> sboard; cin.ignore();
        for (int y = 0; y < HEIGHT; y++) {
            for (int x = 0; x < WIDTH; x++) {
                if (sboard[(y * WIDTH) + x] == '0') connect4.map[x][y] = 0;
                if (sboard[(y * WIDTH) + x] == '1' && id == 2) connect4.map[x][y] = OPP;
                if (sboard[(y * WIDTH) + x] == '1' && id == 1) connect4.map[x][y] = ME;
                if (sboard[(y * WIDTH) + x] == '2' && id == 2) connect4.map[x][y] = ME;
                if (sboard[(y * WIDTH) + x] == '2' && id == 1) connect4.map[x][y] = OPP;
            }
        }
    }

    inline void think() {
        COMMAND = minimax(connect4, MAXDEPTH, ME, 0, true);
    }

    inline void print() {
        cout << COMMAND <<endl;
    }

    inline void debug() {
        connect4.play(COMMAND, id);
        for (int y = 0; y < HEIGHT; y++) {
            for (int x = 0; x < WIDTH; x++) cerr << connect4.map[x][y];
            cerr << endl;
        }
    }
};
int main() {
    state game;
    game.update();
    game.think();
    game.print();
}