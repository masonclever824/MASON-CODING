<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<style>
    .game_form {
        text-align: center;
        margin: 100px;
        font-size: 150%;
    }
</style>

<body>

<?php
//        First shuffle/randomizer algorithm.
//        There are multiple duplicated values to alter the options because otherwise
//        the computer will almost always choose the same values
//        and it is easy to win by learning/guessing the pattern.
$array = ['rock', 'rock', 'rock', 'rock', 'paper', 'paper', 'paper', 'paper', 'scissor', 'scissor', 'scissor', 'scissor'];
shuffle($array);
$computerSelection = $array[3];

//        Second shuffle/randomizer algorithm.
//        $input = ["rock"=>"rock", "paper"=>"paper", "scissor"=>"scissor",
//                  "rock"=>"rock", "paper"=>"paper", "scissor"=>"scissor",
//                  "rock"=>"rock", "paper"=>"paper", "scissor"=>"scissor",
//                  "rock"=>"rock", "paper"=>"paper", "scissor"=>"scissor",
//                  "rock"=>"rock", "paper"=>"paper", "scissor"=>"scissor"];
//        $computerRandomSelection = array_rand($input, 1);
?>

<form class="game_form" action="index.php" method="POST">

    <input type="radio" name="playerSelection" value="rock">Rock<br>
    <input type="radio" name="playerSelection" value="paper">Paper<br>
    <input type="radio" name="playerSelection" value="scissor">Scissor<br>

    <button name="submit">SUBMIT</button>
    <br><br>

    <?php
    if (isset($_POST['playerSelection']) == NULL) {
        echo "Select an option.";
    }

    if (isset($_POST['playerSelection'])) {
        $playerSelection = $_POST['playerSelection'];
        echo "You selected: " . $playerSelection . "<br>";
        echo "Computer selected: " . $computerSelection . "<br>";

        if ($playerSelection == 'rock') {
            if ($computerSelection == 'rock')
                echo "<h1>Draw...</h1>";
            if ($computerSelection == 'paper')
                echo "<h1>You lose.</h1>";
            if ($computerSelection == 'scissor')
                echo "<h1>Winner!</h1>";
        }

        if ($playerSelection == 'paper') {
            if ($computerSelection == 'paper')
                echo "<h1>Draw...</h1>";
            if ($computerSelection == 'rock')
                echo "<h1>Winner!</h1>";
            if ($computerSelection == 'scissor')
                echo "<h1>You lose.</h1>";
        }

        if ($playerSelection == 'scissor') {
            if ($computerSelection == 'scissor')
                echo "<h1>Draw...</h1>";
            if ($computerSelection == 'rock')
                echo "<h1>You lose.</h1>";
            if ($computerSelection == 'paper')
                echo "<h1>Winner!</h1>";
        }
    }
    ?>
</form>

<!--
Just a reference to build the winner vs the looser.
Rock & Rock ===== Draw
Rock & Paper ==== Paper wins
Rock & Scissor == Rock wins

Paper & Paper === Draw
Paper & Rock ==== Paper wins
Paper & Scissor = Scissor wins

Scissor & Scissor = Draw
Scissor & Rock == Rock wins
Scissor & Paper = Scissor wins
-->
</body>
</html>