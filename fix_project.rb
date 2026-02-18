require 'xcodeproj'

project_path = 'ios/Runner.xcodeproj'
project = Xcodeproj::Project.open(project_path)
target = project.targets.find { |t| t.name == 'Runner' }
group = project.main_group.find_subpath('Runner', true)

# Create or find the variant group for InfoPlist.strings
variant_group = group.find_file_by_path('InfoPlist.strings') || 
                group.new_variant_group('InfoPlist.strings')

# Files to add
files = {
  'en' => 'ios/Runner/en.lproj/InfoPlist.strings',
  'tr' => 'ios/Runner/tr.lproj/InfoPlist.strings'
}

files.each do |lang, path|
  unless File.exist?(path)
    puts "Error: File not found at #{path}"
    exit 1
  end

  # Check if reference already exists in the variant group
  ref = variant_group.files.find { |f| f.path == "#{lang}.lproj/InfoPlist.strings" }
  
  if ref
    puts "#{lang} reference already exists."
  else
    # Create reference relative to the group (Runner folder)
    ref = variant_group.new_reference("#{lang}.lproj/InfoPlist.strings")
    ref.name = 'InfoPlist.strings'
    puts "Added #{lang} reference."
  end
  
  # Ensure it is in the "Copy Bundle Resources" build phase
  if target.resources_build_phase.files_references.include?(variant_group)
    puts "#{lang} (Variant Group) is already in Copy Bundle Resources."
  else
    target.resources_build_phase.add_file_reference(variant_group)
    puts "Added Variant Group to Copy Bundle Resources."
  end
end

project.save
puts "Project saved successfully."
