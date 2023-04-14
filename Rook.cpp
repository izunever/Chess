#include "Rook.h"

Rook::Rook(Color color, Position pos) {
    if(color == Color::Black) {
        this->type = "r";
    }
    else {
        this->type = "R";
    }
    this->color=color;
    this->pos = pos;
}

Rook::~Rook() {

}

bool Rook::isValidMove(Position moveToPos) {
    
    return false;
}