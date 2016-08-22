require 'csv'

rows = CSV.foreach("assignment1.csv").to_a

puts rows.inspect

ratings = {}

rows[0][1..-1].each_with_index do |movie, i|
  ratings[movie] = []
  rows[1..-1].each do |row|
    ratings[movie] << row[i+1].to_i if row[i+1]
  end
end

puts ratings.inspect

puts "MEANS:"
means = {}
ratings.each do |movie,ratings|
  means[movie] = ratings.inject(&:+).to_f / ratings.size
end

puts means.inspect
puts means.sort_by(&:last).reverse[0..4].join("\n")

puts "RATINGS:"
rating_counts = {}
ratings.each do |movie,ratings|
  rating_counts[movie] = ratings.size
end

puts rating_counts.inspect
puts rating_counts.sort_by(&:last).reverse[0..4].join("\n")

puts "% >= 4:"
percent_good = {}
ratings.each do |movie,ratings|
  percent_good[movie] = ratings.select { |r| r>=4 }.size.to_f / ratings.size
end

puts percent_good.inspect
puts percent_good.sort_by(&:last).reverse[0..4].join("\n")

puts "Association with Star Wars:"
associations = {}
star_wars_index = rows[0].index("260: Star Wars: Episode IV - A New Hope (1977)")
star_wars_ratings = ratings["260: Star Wars: Episode IV - A New Hope (1977)"].size
rows[0][1..-1].each_with_index do |movie,i|
  both = rows[1..-1].select do |row|
    row[i+1] && row[star_wars_index]
  end.size
  associations[movie] = both.to_f / star_wars_ratings
end

puts associations.inspect
puts associations.sort_by(&:last).reverse[0..4].join("\n")
