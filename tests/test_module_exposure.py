import unittest

from check_module_exposure import module_exposure


MODULE = 'references/domain-lenses.md'
MARKER = 'Distinct candidate method.'


def command(text, output, exit_code=0, event_type='item.completed'):
    return {'type': event_type, 'item': {'id': 'c1', 'type': 'command_execution',
            'command': text, 'aggregated_output': output, 'exit_code': exit_code}}


class ModuleExposure(unittest.TestCase):
    def check_status(self, events, expected):
        self.assertEqual(module_exposure(events, MODULE, MARKER)['status'], expected)

    def test_actual_read_and_distinct_candidate_text(self):
        self.check_status([command('Get-Content -Encoding UTF8 .agents/skills/test/' + MODULE, MARKER)], 'observed')

    def test_same_file_without_candidate_text_is_not_treatment_evidence(self):
        self.check_status([command('Get-Content ' + MODULE, 'Earlier module text.')], 'unverified')

    def test_model_claim_is_not_a_tool_read(self):
        self.check_status([{'type': 'item.completed', 'item': {'type': 'agent_message', 'text': MODULE + MARKER}}], 'unverified')

    def test_echoing_marker_and_path_is_not_a_read(self):
        self.check_status([command('Write-Output "' + MODULE + '"', MARKER)], 'unverified')

    def test_incomplete_command_is_not_completed_evidence(self):
        self.check_status([command('Get-Content ' + MODULE, MARKER, event_type='item.started')], 'unverified')

    def test_read_text_can_exist_before_a_later_command_fails(self):
        result = module_exposure([command('Get-Content ' + MODULE + '; missing-command', MARKER, 1)], MODULE, MARKER)
        self.assertEqual(result['status'], 'observed')
        self.assertEqual(result['matches'][0]['exitCode'], 1)

    def test_other_module_cannot_supply_expected_read(self):
        self.check_status([command('Get-Content references/other.md', MARKER)], 'unverified')


if __name__ == '__main__':
    unittest.main()
