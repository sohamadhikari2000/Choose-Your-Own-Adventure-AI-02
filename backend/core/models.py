from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class StoryOptionLLM(BaseModel):
    text: str = Field(description="the text of the option shown to the user")
    nextNode: Dict[str,Any] = Field(description="the next node content and its options")

class StoryNodeLLM(BaseModel):
    content: str = Field(description="the main content of the story node")
    isEnding: bool = Field(description="whether the story node is ending node or not")
    isWinningEnding: bool = Field(description="whether the story node is winning node or not")
    options: Optional[List[StoryOptionLLM]] = Field(default=None,description="the options of the story node")

class StoryLLMResponse(BaseModel):
    title:str = Field(description="the title of the story")
    rootNode: StoryNodeLLM = Field(description="the root node of the story")
