from pyrouge import Rouge155    
rouge = Rouge155()
rouge.system_dir = 'tests/data/systems'
rouge.model_dir = 'tests/data/models'

# The system filename pattern should contain one group that
# matches the document ID.
rouge.system_filename_pattern = 'SL.P.10.R.11.SL062003-(\d+).html'

# The model filename pattern has '#ID#' as a placeholder for the
# document ID. If there are multiple model summaries, pyrouge
# will use the provided regex to automatically match them with
# the corresponding system summary. Here, [A-Z] matches
# multiple model summaries for a given #ID#.
rouge.model_filename_pattern = 'SL.P.10.R.[A-Z].SL062003-#ID#.html'

rouge_output = rouge.evaluate()
print(rouge_output)
output_dict = rouge.output_to_dict(rouge_output)
print(output_dict)
