from src import settings
# from src.classes.evaluators import EvaluatorConfigSimple, EvaluatorSimple
from src.classes.evaluators import EvaluatorSimple
from src.classes.results import ResultsOfEvaluatorSimple
from os.path import join
from src.classes import utils


if __name__ == '__main__':
    # evaluator_config = EvaluatorConfigSimple()
    # evaluator = EvaluatorSimple(config=evaluator_config)
    evaluator = EvaluatorSimple()
    results: ResultsOfEvaluatorSimple = evaluator.get_results()
    output_results_unique_filepath = join(
        settings.Files.OUTPUT_DIRPATH,
        utils.generate_unique_filename()
    )
    results.to_csv(output_results_unique_filepath)
    print()
    print('=' * 40)
    print('results:')
    print(results)
    print('=' * 40)
    print('# of games:', len(results))
    print('# of wins:')
    print(results.sum())
    print('# of wins / # of games:')
    print(results.sum() / len(results))
