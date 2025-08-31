from commitizen.cz.conventional_commits.conventional_commits import ConventionalCommitsCz
from commitizen.question import CzQuestion


class AnidroneConventionalCommitsCz(ConventionalCommitsCz):
    """
    Start with everything from 'ConventionalCommitsCz' and override what you need.
    """

    def questions(self) -> list[CzQuestion]:
        result = super().questions()

        if "choices" in result[0] and isinstance(result[0]["choices"], list):
            result[0]["choices"].append(
                {
                    "value": "cad",
                    "name": "cad: CAD/UX/architecture changes",
                    "key": "a",
                }
            )
            result[0]["choices"].append(
                {
                    "value": "dev",
                    "name": "dev: A change to the development environment, process or tooling",
                    "key": "v",
                }
            )
        return result
