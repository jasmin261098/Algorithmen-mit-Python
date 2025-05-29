evenNumberCounter :: [Int] -> Int
evenNumberCounter numbers = length (filter even numbers)

main :: IO ()
main = do
    let numbers = [1, 2, 3, 4, 5, 6]
    print (evenNumberCounter numbers)