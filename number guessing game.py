{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d75118ab-7cac-465f-b9bb-e305180e4e44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "THE NUMBER GUESSING GAME\n",
      "1. Easy\n",
      "2. Medium\n",
      "3. Hard\n",
      "4. Insane\n",
      "5. Impossible\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose difficulty:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "guess from -1000 - 1000 ( ONLY FIVE ATTEMPTS)\n",
      "number of attempts: 1\n",
      "number of attempts remaining: 4\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your guess:  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "guess lower\n",
      "number of attempts: 2\n",
      "number of attempts remaining: 3\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your guess:  -500\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "guess lower\n",
      "number of attempts: 3\n",
      "number of attempts remaining: 2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your guess:  -750\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "guess higher\n",
      "number of attempts: 4\n",
      "number of attempts remaining: 1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your guess:  -600\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "guess lower\n",
      "number of attempts: 5\n",
      "number of attempts remaining: 0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your guess:  -699\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "guess higher\n",
      "you're out of attempts :<\n",
      "better luck next time!! ;)\n",
      "the number was -607\n"
     ]
    }
   ],
   "source": [
    "## number guessing game\n",
    "# by thakur yashraj singh\n",
    "\n",
    "import random as rn\n",
    "\n",
    "print(\"THE NUMBER GUESSING GAME\")\n",
    "\n",
    "print(\"1. Easy\")\n",
    "print(\"2. Medium\")\n",
    "print(\"3. Hard\")\n",
    "print(\"4. Insane\")\n",
    "print(\"5. Impossible\")\n",
    "\n",
    "level = int(input(\"Choose difficulty: \"))\n",
    "\n",
    "a = 0\n",
    "b = 0\n",
    "c = 0\n",
    "ic = 0\n",
    "\n",
    "if level == 1:\n",
    "    print(\"guess from 1-100\")\n",
    "    a = 0\n",
    "    b = 100\n",
    "    c = 100\n",
    "    ic = 75\n",
    "\n",
    "elif level == 2:\n",
    "    print(\"guess from 1-500\")\n",
    "    a = 0\n",
    "    b = 500\n",
    "    c = 100\n",
    "    ic = 375\n",
    "\n",
    "elif level == 3:\n",
    "    print(\"guess from 1-1000\")\n",
    "    a = 0\n",
    "    b = 1000\n",
    "    c = 100\n",
    "    ic = 750\n",
    "\n",
    "elif level == 4:\n",
    "    print(\"guess from -1000 - 1000\")\n",
    "    a = -1000\n",
    "    b = 1000\n",
    "    c = 100\n",
    "    ic = 1500\n",
    "\n",
    "elif level == 5:\n",
    "    print(\"guess from -1000 - 1000 ( ONLY FIVE ATTEMPTS)\")\n",
    "    a = -1000\n",
    "    b = 1000\n",
    "    c = 5\n",
    "    ic = 1500\n",
    "\n",
    "else:\n",
    "    print(\"there's no such level\", level)\n",
    "    exit()\n",
    "\n",
    "n = rn.randint(a, b)\n",
    "\n",
    "for i in range(1, c + 1):\n",
    "\n",
    "    print(\"number of attempts:\", i)\n",
    "    print(\"number of attempts remaining:\", c - i)\n",
    "\n",
    "    num = int(input(\"enter your guess: \"))\n",
    "\n",
    "    if num > n:\n",
    "        print(\"guess lower\")\n",
    "\n",
    "        if num > n + ic:\n",
    "            print(\"that's way too high\")\n",
    "\n",
    "    elif num < n:\n",
    "        print(\"guess higher\")\n",
    "\n",
    "        if num < n - ic:\n",
    "            print(\"that's way too less\")\n",
    "\n",
    "    elif num == n:\n",
    "        print(\"correct answer\")\n",
    "        print(\"the number was\", n)\n",
    "        break\n",
    "\n",
    "else:\n",
    "    print(\"you're out of attempts :<\")\n",
    "    print(\"better luck next time!! ;)\")\n",
    "    print(\"the number was\", n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37a36c30-3cdc-4a1b-a1f9-4ab37359b17b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
