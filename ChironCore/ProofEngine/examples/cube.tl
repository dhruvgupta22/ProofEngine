assume(1==1)
:c1 = :a*:a*:a - 3*:a*:a*:b + 3*:a*:b*:b - :b*:b*:b
:c2 = (:a-:b)*(:a-:b)*(:a-:b)
assert(:c1 == :c2)