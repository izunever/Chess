#include "BasePiece.h"
#include <iostream>
#include <string>

using namespace std;

BasePiece::BasePiece() {
    type = " ";
}

BasePiece::~BasePiece() {
}

void BasePiece::printPiece() {
    if (color == Color::Black) {
        cout << "b";
    }
    else {
        cout << "w";
    }
    cout << type; 
}

void BasePiece::setPosition(Position pos) {
    this->pos = pos;
}

Position BasePiece::getPosition() {
    return pos;
}

Color BasePiece::getColor() {
    return color;
}